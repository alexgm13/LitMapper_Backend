from app.api.routes import proyecto_tema_router, user_route, proyecto_pico_router, articulo_router, proyecto_router


all_routes = [
    user_route.router,
    proyecto_pico_router.router,
    proyecto_tema_router.router,
    articulo_router.router,
    proyecto_router.router
]