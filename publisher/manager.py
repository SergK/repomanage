import logging

from oslo_config import cfg

# from publisher import errors

opts = [
    cfg.StrOpt(
        'tmp_path',
        default='/tmp',
        help='Temporary directory for file manipulations',
    ),
    cfg.IntOpt(
        'simple_count',
        default=7,
        help='Just simple count'
    ),
]

cli_opts = [
    cfg.StrOpt(
        'hello',
        default='world',
        help='Hellow world'
    ),
    cfg.StrOpt(
        'Temporary directory',
        default='/tmp',
        help='Directory where we store temp stuff',
    ),
]

CONF = cfg.CONF
CONF.register_opts(opts)
CONF.register_cli_opts(cli_opts)

LOG = logging.getLogger(__name__)


class Manager(object):
    def __init__(self, data):
        print(data)

    def do_create_empty_repo(self):
        LOG.debug('--- do_create_empty_repo ---')

    def do_add_package_to_repo(self):
        LOG.debug('--- do_add_package_to_repo ---')

    def do_remove_package_from_repo(self):
        LOG.debug('--- do_remove_package_from_repo ---')

    def do_update_repo(self):
        LOG.debug('--- do_update_repo ---')
