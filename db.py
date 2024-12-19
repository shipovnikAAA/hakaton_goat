


from supabase import create_client, Client

url: str = "https://kewhguvjbntiivskcfwf.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imtld2hndXZqYm50aWl2c2tjZndmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzQ1OTE0MDYsImV4cCI6MjA1MDE2NzQwNn0.lVtllKPa8aZcSQTrjPnRJfgiLhUOypI_nWKDJp_US1s"
supabase: Client = create_client(url, key)

def add_player(login, name, rating, password):
    try:
        response = ((supabase.table("players")
                    .insert({"name": name, "rating": rating, "password": password, "login": login}))
                    .execute())
        return response

    except Exception as exception:
        return exception

def get_player(login, password):
    response = (supabase.table("players")
                .select("*")
                .eq("login", login)
                .eq("password", password)
                .execute())
    return response

def get_ratings():
    response = (supabase.table("players")
                .select("name, rating")
                .order("rating", desc=True)
                .execute())
    return response

def get_questions():
    response = (supabase.table("questions")
                .select("*")
                .execute())
    return response

def update_rating(rating, login):
    try:
        response = ((supabase.table("players")
                    .update({"rating": rating})
                    .eq("login", login))
                    .execute())
        return response

    except Exception as exception:
        return exception

