import os
from minitage.core.common import append_env_var
import shutil
def h(options, buildout):
    """."""
    dest = buildout['part']['location']
    [shutil.copy2(os.path.join(dest, 'libexec', f),
                  os.path.join(dest, 'bin', f))
     for f in os.listdir(os.path.join(dest, 'libexec'))]
# vim:set ts=4 sts=4 et  :
