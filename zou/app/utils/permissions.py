from flask_principal import RoleNeed, Permission
from werkzeug.exceptions import Forbidden
from zou.app.services import persons_service

admin_permission = Permission(RoleNeed("admin"))
manager_permission = Permission(RoleNeed("manager"))
client_permission = Permission(RoleNeed("client"))


class PermissionDenied(Forbidden):
    pass


def has_manager_permissions():
    """
    Return True if user is admin or manager.
    """
    return admin_permission.can() or manager_permission.can()


def has_admin_permissions():
    """
    Return True if user is admin or manager.
    """
    return admin_permission.can()


def has_client_permissions():
    """
    Return True if user is client.
    """
    return client_permission.can()


def check_manager_permissions():
    """
    Return True if user is admin or manager. It raises a PermissionDenied
    exception in case of failure.
    """
    if has_manager_permissions():
        return True
    else:
        raise PermissionDenied


def check_admin_permissions():
    """
    Return True if user is admin. It raises a PermissionDenied exception in case
    of failure.
    """
    if admin_permission.can():
        return True
    else:
        raise PermissionDenied
