def request_finished(sender, **kwargs):
    print "finished", kwargs

def model_saved(sender, **kwargs):
    print "SAVED", sender, kwargs