import uvicorn
import sys
from settings import settings
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

if '__main__' == __name__:
    uvicorn.run(
        'app:app',
        host=settings.service_host,
        port=settings.service_port,
        reload=True
    )