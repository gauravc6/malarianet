import warnings
from malarianet import app

if __name__ == '__main__':
    app.run(debug=True)

    
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        warnings.warn("deprecated", DeprecationWarning)
