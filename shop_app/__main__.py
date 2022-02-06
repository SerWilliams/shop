import uvicorn
from settings import settings


if '__main__' == __name__:
    uvicorn.run(
        'app:app',
        host=settings.service_host,
        port=settings.service_port,
        reload=True
    )