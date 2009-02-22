import sys

import enso.platform

if sys.platform != "darwin":
    raise enso.platform.PlatformUnsupportedError()

def get_script_folder_name():
  """Returns the folder where Enso commands are found. This function
     is responsible for ensuring that this folder exists: it must not
     return a path that is not present! It is expected to place this
     folder in some platform-specific logical location."""
  raise NotImplementedError("This platform does not define a "
      "scripts folder (this needs fixing)")


def provideInterface( name ):
    if name == "input":
        import enso.platform.osx.input
        return enso.platform.osx.input
    elif name == "graphics":
        import enso.platform.osx.graphics
        return enso.platform.osx.graphics
    elif name == "cairo":
        import enso.platform.osx.cairo
        return enso.platform.osx.cairo
    elif name == "selection":
        import enso.platform.osx.selection
        return enso.platform.osx.selection
    elif name == "scripts_folder":
        return get_script_folder_name
    else:
        return None
