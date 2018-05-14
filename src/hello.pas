PROGRAM teste;

VAR
    x, y, z: int;
    test: bool;
BEGIN
    BEGIN
        BEGIN

            y := 3;
            test := 1 + 2;

            IF (y < 3) THEN
                BEGIN
                    x := not 1;
                    Print(x);
                END
            ELSE
                BEGIN
                    x := not 2;
                    Print(test);
                END;

            WHILE (y < 3) DO
                BEGIN
                    Print(x);
                END
        END
    END
END.