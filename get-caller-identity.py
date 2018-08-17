#!/usr/bin/env python
import boto3

access_key = 'AKIAJFGARNMXDRHJX6WA'
secret_key = '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'

def get_aws_account_id(access_key, secret_key):
    sts = boto3.client(
        "sts", aws_access_key_id=access_key, aws_secret_access_key=secret_key,
    )
    user_arn = sts.get_caller_identity()["Arn"]

    return user_arn.split(":")[4]

print get_aws_account_id(access_key, secret_key)
