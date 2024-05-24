from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

from src.routers import health_checker_router, user_router
from src.repo.conn import Base

provider = TracerProvider(resource=Resource.create({SERVICE_NAME: "Fastapi-users"}))
processor = BatchSpanProcessor(
    JaegerExporter(
        agent_host_name="jaeger",
        agent_port=6831
    )
)
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

app = FastAPI()
FastAPIInstrumentor.instrument_app(app, excluded_urls="/health,/docs,/openapi.json")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["Content-Type"],
    allow_credentials="true",
)

app.include_router(user_router)
app.include_router(health_checker_router)
