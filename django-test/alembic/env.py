from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from sqlalchemy_models import Base, FunnyAnimal
from alembic import context
import os
import re

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Construct the database URL from environment variables
db_user = os.getenv("SQL_USER")
db_password = os.getenv("SQL_PASSWORD")
db_name = os.getenv("SQL_DATABASE")
db_host = os.getenv("SQL_HOST")
db_port = os.getenv("SQL_PORT")
database_url = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Update the alembic config with the database URL
config.set_main_option("sqlalchemy.url", database_url)

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

# The pattern to exclude the django ORM tables
django_tables_pattern = re.compile(r'(^django_)|(^auth_)|(^testdb_)')


def include_object(object, name, type_, reflected, compare_to):
    # Exclude tables that match the Django naming pattern
    if type_ == "table" and django_tables_pattern.match(name):
        return False
    return True


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        include_object=include_object,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_object=include_object
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
