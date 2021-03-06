# Copyright 2015-2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import logging

from flask import request
from requests import HTTPError
from xivo import auth_verifier

from wazo_call_logd.core.exceptions import TokenWithUserUUIDRequiredError

logger = logging.getLogger(__name__)
required_acl = auth_verifier.required_acl
extract_token_id_from_query_or_header = auth_verifier.extract_token_id_from_query_or_header


def get_token_user_uuid_from_request(auth_client):
    token = request.headers.get('X-Auth-Token') or request.args.get('token')
    try:
        token_infos = auth_client.token.get(token)
    except HTTPError as e:
        logger.warning('HTTP error from xivo-auth while getting token: %s', e)
        raise TokenWithUserUUIDRequiredError()
    user_uuid = token_infos['xivo_user_uuid']
    if not user_uuid:
        raise TokenWithUserUUIDRequiredError()
    return user_uuid
