# cloud_run_sidecar

```
bash build.sh

# Upload the IMAGES
docker push SIDECAR-IMAGE
docker push FOO-IMAGE

# Deploy sidecar alone as a cloud run service
gcloud run deploy debugging-sidecar-alone \
  --image SIDECAR-IMAGE \
  --region us-west2 \
  --no-allow-unauthenticated

# Test sidecar image as a standalone cloud run. The following will return
# "sidecar" immediately
curl -X POST https://debugging-sidecar-alone-RANDOM-STRING/sidecar \
  -H "Content-type: Application/json" -d '{}' \
  -H "Authorization: Bearer $(gcloud auth print-identity-token)"

# Change FOO-IMAGE and SIDECAR-IMAGE properly before running the command
# Deploy foo and sidecar as a cloud run service
gcloud run services replace service.yaml --region=us-west2

# Test sidecar image as a sidecar. It will fail with 500 error within the
# few minutes of the deployment. And in the logs, you can see the message
# "Serving on http://0.0.0.0:5000" after a few minutes of deployment
curl -X POST https://debugging-foo-sidecar-RANDOM-STRING/foo \
  -H "Content-type: Application/json" -d '{}' \
  -H "Authorization: Bearer $(gcloud auth print-identity-token)"
```
