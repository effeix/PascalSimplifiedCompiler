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
    x := 30;
    y:= x - 15;

    write(10 and 20);

    WHILE (y > 2) DO
    BEGIN
        x := x + 2;
        write(x);
        y := y - 2;
    END;

    IF (x > 1) THEN
    BEGIN
        write(12234);
        write(not x);
    END;
END.