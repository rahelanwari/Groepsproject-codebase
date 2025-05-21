import os
from supabase import create_client, Client

SUPABASE_URL = os.environ.get("https://vkqkqbjyfuvzpsqsutka.supabase.co")
SUPABASE_SERVICE_KEY = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZrcWtxYmp5ZnV2enBzcXN1dGthIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0NzIwODg1MywiZXhwIjoyMDYyNzg0ODUzfQ.RpsMVyF-ZByjj2a_FNQcDuWdp4txLWHYd4tA4ZKvEO8")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)
