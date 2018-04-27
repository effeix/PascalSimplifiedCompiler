PROGRAM teste;

BEGIN
    BEGIN
        BEGIN
            x := (15 | 8); 
            y := 3 + x;
            Print(x+y);
            Print(3);
            Print(x);
            z := 5;
            
            IF (2>3) THEN BEGIN 
                Print(2); 
            END;

            WHILE (z > 1) DO BEGIN
                z := z - 1;
                print(42);
            END;

            WHILE (x > 1) DO BEGIN
                x := x - 1;
                print(54321);
            END;
        END
    END
END.
