"""List of API Enpoints the moco wrapper knows about."""

API_PATH = {
    "employment_get":                   "/users/employments/{id}",
    "employment_getlist":               "/users/employments",
    "holiday_getlist":                  "/users/holidays",
    "holiday_get":                      "/users/holidays/{id}",
    "holiday_create":                   "/users/holidays",
    "holiday_update":                   "/users/holidays/{id}",
    "holiday_delete":                   "/users/holidays/{id}",
    "hourly_rate_get":                  "/account/hourly_rates",
    "presence_getlist":                 "/users/presences",
    "presence_get":                     "/users/presences/{id}",
    "presence_create":                  "/users/presences",
    "presence_update":                  "/users/presences/{id}",
    "presence_touch":                   "/users/presences/touch",
    "presence_delete":                  "/users/presences/{id}",
    "project_task_getlist":             "/projects/{project_id}/tasks",
    "project_task_get":                 "/projects/{project_id}/tasks/{task_id}",
    "project_task_create":              "/projects/{project_id}/tasks",
    "project_task_update":              "/projects/{project_id}/tasks/{task_id}",
    "project_task_delete":              "/projects/{project_id}/tasks/{task_id}",
    "unit_get":                         "/units/{id}",
    "unit_getlist":                     "/units",
    "schedule_get":                     "/schedules/{id}",
    "schedule_getlist":                 "/schedules",
    "schedule_create":                  "/schedules",
    "schedule_update":                  "/schedules/{id}",
    "schedule_delete":                  "/schedules/{id}",
    "purchase_category_get":            "/purchases/categories/{id}",
    "purchase_category_getlist":        "/purchases/categories",
    "tagging_add":                      "/taggings/{entity}/{entity_id}",
    "tagging_replace":                  "/taggings/{entity}/{entity_id}",
    "tagging_delete":                   "/taggings/{entity}/{entity_id}",
    "tagging_get":                      "/taggings/{entity}/{entity_id}",
}
