#!/usr/bin/env bash
set -e
if [ "$SELENIUM_MODE" = "grid" ] ; then
    echo "Waiting for Selenium Hub at $SELENIUM_REMOTE_URL..."
    for i in $(seq 1 30) ; do
        if curl -sSf "$SELENIUM_REMOTE_URL/status" > /dev/null 2>&1 ; then
            echo "Selenium Hub is available!"
            break
        fi
        echo "Waiting... ($i)"
        sleep 2
    done
fi
exec "$@"