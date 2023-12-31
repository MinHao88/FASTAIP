import importlib
import os
from pathlib import Path

import pytest

from ...utils import needs_pydanticv1


# TODO: pv2 add version with Pydantic v2
@needs_pydanticv1
def test_testing_dbs(tmp_path_factory: pytest.TempPathFactory):
    tmp_path = tmp_path_factory.mktemp("data")
    cwd = os.getcwd()
    os.chdir(tmp_path)
    test_db = Path("./test.db")
    if test_db.is_file():  # pragma: nocover
        test_db.unlink()
    # Import while creating the client to create the DB after starting the test session
    from docs_src.sql_databases.sql_app.tests import test_sql_app

    # Ensure import side effects are re-executed
    importlib.reload(test_sql_app)
    test_sql_app.test_create_user()
    if test_db.is_file():  # pragma: nocover
        test_db.unlink()
    os.chdir(cwd)
