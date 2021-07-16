#!/bin/bash

for i in "$@"
do
case $i in
    -s=*|--secret=*)
    SECRET="${i#*=}"
    shift
    ;;
    -t=*|--token=*)
    TOKEN="${i#*=}"
    shift
    ;;
    *)
          # unknown option
    ;;
esac
done

c="gcloud secrets versions access latest --secret=${SECRET} --format='get(payload.data)' | tr '_-' '/+' | base64 -d > ${TOKEN}"
eval ${c}