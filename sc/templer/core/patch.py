# -*- coding:utf-8 -*-
from paste.script import copydir

def sub_catcher(filename, vars, func, *args, **kw):
    """
    Run a substitution, returning the value.  If an error occurs, show
    the filename.  If the error is a NameError, show the variables.
    """
    try:
        return func(*args, **kw)
    except copydir.SkipTemplate, e:
        print 'Skipping file %s' % filename
        if str(e):
            print str(e)
        raise
    except UnicodeEncodeError:
        return args[0].respond().encode('utf-8')
    except Exception, e:
        print 'Error in file %s:' % filename
        if isinstance(e, NameError):
            items = vars.items()
            items.sort()
            for name, value in items:
                print '%s = %r' % (name, value)
        raise

def run():
    ''' Overwrite sub_catcher function on paste.script.copydir '''
    setattr(copydir, '_sub_catcher', copydir.sub_catcher)
    setattr(copydir, 'sub_catcher', sub_catcher)    