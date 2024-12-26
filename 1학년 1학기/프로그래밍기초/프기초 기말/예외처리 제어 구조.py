class NonPositive(Exception): pass

def factorical():
    while True:
        try:
            n = int(input("Enter a number: "))
            assert n >= 0
            
        except ValueError:
            print("Not a number")
        
        except SyntaxError:
            pass
        
        except TypeError:
            pass
        
        except NameError:
            pass
        
        except IndexError:
            pass
        
        except KeyError:
            pass
        
        except ZeroDivisionError:
            pass
        
        except FileNotFoundError:
            pass
        
        except AssertionError:
            print("Not a natural number.")
            
        except NonPositive:
            print("Not a natural number.")
            
        else:
            print("ddd", n, sep= '')
            
            break
        finally:
            print("d")