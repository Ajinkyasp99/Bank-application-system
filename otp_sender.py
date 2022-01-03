import requests
import random

num = {"Phone no": request.form["phone"]}
    otp = random.randint(123456, 999999)
    msg = "Your otp is " + str(otp)
    URL = f'https://www.fast2sms.com/dev/bulkV2?authorization=ncU8ARFdqzC06alm47fWMkNJYDKe5ZV9g3sxt2oHPvBEOywXLQyXrsgaY4tACJkMPOZKEuI9o2nxDB57&variables_values={otp}"&route=otp&numbers={num}'

    r = requests.get(url=URL)

    get_otp = {"otp":request.form["otp"]}

    if otp == get_otp:
        resp = "Account Register Successfully"
        return resp
    else:
        resp ="Please Enter valid otp"
        return resp
    return render_template("send_otp.html",message =str(resp))