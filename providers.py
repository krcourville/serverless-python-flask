from flask_injector import request
from injector import Binder, Module, provider

from infrastructure.repositories.UserRepository import UserRepository


class RepositoriesModule(Module):
    @request
    @provider
    def provide_user_repository(self) -> UserRepository:
        return UserRepository()


def configure(binder: Binder):
    binder.bind()