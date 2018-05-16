PROGRAM a;

VAR
    x, y, z: integer;
    test: boolean;

FUNCTION test_a(): integer;
BEGIN
    write(1);
END;

FUNCTION test_b(): integer;
BEGIN
    write(2);
END;

BEGIN
    x := 0;
    y:= 10;

    write(1 AND 2);

    WHILE (y > 0) DO
    BEGIN
        x := x + 2;
        write(x);
        y := y - 1;
    END;

    IF (x > 1) THEN
    BEGIN
        write(not x);
    END;
END.