from django.shortcuts import redirect

class LogoutRequiredMixin(object):
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')

        return super(LogoutRequiredMixin, self).dispatch(*args, **kwargs)