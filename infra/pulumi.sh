#!/bin/bash

for i in "$@"
do
case $i in
    -b=*|--build_type=*)
    BUILD_TYPE="${i#*=}"
    shift
    ;;
    -p=*|--project=*)
    PROJECT="${i#*=}"
    shift
    ;;
    -s=*|--stack=*)
    STACK="${i#*=}"
    shift
    ;;
    *)
          # unknown option
    ;;
esac
done

# exit if a command returns a non-zero exit code and also print the commands and their args as they are executed.
set -e -x

export PULUMI_CONFIG_PASSPHRASE=""

# Login into pulumi. This will require the PULUMI_ACCESS_TOKEN environment variable.
pulumi login --cloud-url gs://pulumi-state-${PROJECT}

if [ "${BUILD_TYPE}" = "destroy" ]; then
    echo "pulumi destroy ${STACK}"
    pulumi stack select ${STACK}
    pulumi destroy --non-interactive --yes
elif [ "${BUILD_TYPE}" = "init" ]; then
    echo "pulumi init ${STACK}"
    pulumi stack init ${STACK} --secrets-provider=passphrase
elif [ "${BUILD_TYPE}" = "remove" ]; then
    echo "pulumi remove ${STACK}"
    pulumi stack select ${STACK}
    pulumi stack rm ${STACK} --non-interactive --yes
elif [ "${BUILD_TYPE}" = "up" ]; then
    echo "pulumi up ${STACK}"
    pulumi stack select ${STACK}
    pulumi up --non-interactive --yes
else
    echo "pulumi preview ${STACK}"
    pulumi stack select ${STACK}
    pulumi preview --non-interactive --diff
fi
