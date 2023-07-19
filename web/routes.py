import views

url_pattern = {
    "/api/view": views.api_view,
    "/api/get": views.api_get,

    "/": views.home_view,
    "/about":views.about_view

}


post_url_pattern = {
    "/api/post/test":views.api_post
}