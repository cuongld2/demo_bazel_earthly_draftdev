import sys
import uvicorn

if __name__ == "__main__":
    # freeze_support()
    sys.argv.insert(1, "user_app.main:app")
    sys.exit(uvicorn.main())  # pylint: disable=no-value-for-parameter
