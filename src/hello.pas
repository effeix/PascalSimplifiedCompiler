PROGRAM test_all;

VAR
    a, b, c, integer_return: integer;
    boolean_return: boolean;

FUNCTION function_integer_return(x: integer): integer;
    VAR
        a, b: integer;

    BEGIN
        a := 1;
        b := 2;
        write(a + b + b);
        function_integer_return := x;
    END;

FUNCTION function_boolean_return(y,x: boolean): boolean;
    VAR
        a, b: boolean;
    BEGIN
        a := true;
        b := false;
        write(a and b);
        function_boolean_return := y and x;
    END;

BEGIN
    c := read();
    write(c);

    write(1 and 2);
    write(1 and 1);
    write(not -3);
    write(function_integer_return(39));

    write(true and true);
    write(true or false);
    write(not true);
    write(function_boolean_return(true, false));

    a := 0;
    b := 10;

    WHILE (b > 0) DO
    BEGIN
        IF (b > 5) THEN
            BEGIN
                write(123456789);
            END
        ELSE
            BEGIN
                write(987654321);
            END;

        b := b - 1;
    END;
END.