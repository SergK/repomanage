import logging
import sys

from oslo_config import cfg
import six

import manager
import version

cli_opts = [
    cfg.StrOpt(
        'input_data_file',
        default='/tmp/publisher.config',
        help='Input data file'
    ),
    cfg.StrOpt(
        'input_data',
        default='',
        help='Input data (json string)'
    ),
]

CONF = cfg.CONF
CONF.register_cli_opts(cli_opts)


def create_empty_repo():
    main(['do_create_empty_repo'])


def add_package_to_repo():
    main(['do_add_package_to_repo'])


def remove_package_from_repo():
    main(['do_remove_package_from_repo'])


def update_repo():
    main(['do_update_repo'])


def print_err(line):
    sys.stderr.write(six.text_type(line))
    sys.stderr.write('\n')


def handle_exception(exc):
    LOG = logging.getLogger(__name__)
    LOG.exception(exc)
    print_err('Unexpected error')
    print_err(exc)
    sys.exit(-1)


def main(actions=None):
    CONF(sys.argv[1:], project='publisher',
         version=version.version_info.release_string())

    logging.basicConfig(level=logging.INFO)
    LOG = logging.getLogger(__name__)

    try:
        if CONF.input_data:
            # data = json.loads(CONF.input_data)
            print("hello")
            data = "Hello-data"
        else:
            with open(CONF.input_data_file) as f:
                text = f.read()
                data = "Bye-data"
                print("Bye")
                print(text)
        LOG.debug('Input data: %s', data)

        mgr = manager.Manager(data)
        if actions:
            for action in actions:
                getattr(mgr, action)()
    except Exception as exc:
        handle_exception(exc)


if __name__ == '__main__':
    main()
