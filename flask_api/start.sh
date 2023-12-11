#!/usr/bin/env bash
gunzip -k functions/pickles/sig.gz
gunicorn -w 4 wsgi:application