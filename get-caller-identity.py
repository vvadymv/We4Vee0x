#!/usr/bin/env python
import boto3

access_key = 'AKIAJODMFAHUEVVVKKIQ'
secret_key = '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'

def get_aws_account_id(access_key, secret_key):
    sts = boto3.client(
        "sts", aws_access_key_id=access_key, aws_secret_access_key=secret_key,
    )
    user_arn = sts.get_caller_identity()["Arn"]

    return user_arn.split(":")[4]

print get_aws_account_id(access_key, secret_key)
