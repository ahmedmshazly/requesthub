# Define project name
$projectName = "requesthub"

# Create project directory
New-Item -ItemType Directory -Name $projectName | Out-Null
Set-Location -Path $projectName

# Create subdirectories
$directories = "assets", "src", "views", "controllers", "models", "utils", "tests"
foreach ($dir in $directories) {
    New-Item -ItemType Directory -Name $dir | Out-Null
}

# Create files
$files = "README.md", "requirements.txt"
foreach ($file in $files) {
    New-Item -ItemType File -Name $file | Out-Null
}

# Create source files
$sourceFiles = "src/__init__.py", "src/main.py", "src/authentication.py", "src/interfaces.py", "src/database.py"
foreach ($file in $sourceFiles) {
    New-Item -ItemType File -Name $file | Out-Null
}

# Create view files
$viewFiles = "views/login_view.py", "views/signup_view.py", "views/dashboard_view.py"
foreach ($file in $viewFiles) {
    New-Item -ItemType File -Name $file | Out-Null
}

# Create controller files
$controllerFiles = "controllers/login_controller.py", "controllers/signup_controller.py", "controllers/dashboard_controller.py"
foreach ($file in $controllerFiles) {
    New-Item -ItemType File -Name $file | Out-Null
}

# Create model and util files
$modelFile = "models/user_model.py"
$utilFile = "utils/validation.py"
New-Item -ItemType File -Name $modelFile | Out-Null
New-Item -ItemType File -Name $utilFile | Out-Null

# Create __init__.py files
$initFiles = "src/__init__.py", "views/__init__.py", "controllers/__init__.py", "models/__init__.py", "utils/__init__.py"
foreach ($file in $initFiles) {
    New-Item -ItemType File -Name $file | Out-Null
}

# Print success message
Write-Host "Project structure created successfully!"
