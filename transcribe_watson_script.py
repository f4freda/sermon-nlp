curl -X POST -u INSERT_YOUR_IBM_WATSON_USER_KEY \
--header "Content-Type: audio/mp3" \
--header "Transfer-Encoding: chunked" \
--data-binary @AUDIO_FILE_NAME.mp3 \
"https://stream.watsonplatform.net/speech-to-text/api/v1/recognize" &> TRANSCRIPT_FILENAME.txt