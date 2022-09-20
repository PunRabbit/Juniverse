from abc import ABCMeta


class ConfigClass(metaclass=ABCMeta):
    """
    This Class only for Serving Hint for Dataclass that using for Config.
    """
    pass


class TemplateClass(metaclass=ABCMeta):
    """
    This Class only for Serving Hint for Dataclass that using for Template (Alarm or Something).
    """
    pass


class CompactConfigClass(metaclass=ABCMeta):
    """
    Combine All ConfigClasses.
    """
    pass

