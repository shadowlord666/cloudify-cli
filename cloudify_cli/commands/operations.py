########
# Copyright (c) 2018 Cloudify Platform Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
############


from ..cli import cfy
from ..table import print_data


OPERATION_COLUMNS = ['id', 'execution', 'name', 'state']


@cfy.group(name='operations')
@cfy.options.common_options
@cfy.assert_manager_active()
def operations():
    """Handle an execution's operations
    """
    pass


@operations.command(name='list')
@cfy.argument('execution', required=True)
@cfy.options.common_options
@cfy.pass_logger
@cfy.pass_client()
def list(execution, client, logger):
    logger.info('Listing operations...')
    agents = client.operations.list(execution)
    print_data(OPERATION_COLUMNS, agents, 'Operations:')
