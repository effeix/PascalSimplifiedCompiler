PROGRAM teste;

VAR
    x, y, z: integer;
    test: boolean;
BEGIN
    BEGIN
        BEGIN

            x:=30;
            y:=x-15;

            while (y > (10 or 20)) do begin
                x:= x+2;
                print(x);
                y:= y-2;
            end;

            if (x > 1) then
            begin
                print(not(not x));
            end;
        END
    END
END.