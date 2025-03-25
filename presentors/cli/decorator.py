from infrastructure.di import container
from dishka.integrations.base import wrap_injection

def inject(**kwargs):
    def decorator(func):
        return wrap_injection(
            func=func,
            container_getter=lambda _, __: container,
            **kwargs
        )
    return decorator