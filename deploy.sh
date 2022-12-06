echo "I am hello"
cd testdeploymentviagithub
echo "$(ls)"
docker-compose -f docker-compose.yml up -d api
