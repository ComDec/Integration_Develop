import coverage
import pytest

cov = coverage.Coverage(branch=True)
cov.start()

pytest.main()

cov.stop()
cov.save()

cov.report()
