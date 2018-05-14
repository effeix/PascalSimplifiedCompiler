PROGRAM teste;

VAR
    x, y, z: integer;
    test: boolean;
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
        write(not(not x));
    END;
END.