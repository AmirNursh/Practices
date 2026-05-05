CREATE OR REPLACE FUNCTION search_pattern(pattern TEXT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.name, p.phone
    FROM phonebook p
    WHERE p.name ILIKE '%' || pattern || '%'
       OR p.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;