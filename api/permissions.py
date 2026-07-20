from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminTeacherOrReadOnly(BasePermission):

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        # Everyone can perform safe methods
        if request.method in SAFE_METHODS:
            return True

        # Admin can do everything
        if request.user.role == "ADMIN":
            return True

        # Teacher can Create & Update
        if request.user.role == "TEACHER":

            if request.method in ["POST", "PUT", "PATCH"]:
                return True

        return False


class IsAdminOnly(BasePermission):

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated
            and request.user.role == "ADMIN"
        )