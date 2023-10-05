from flask import  jsonify, request, Blueprint
from models import PersonalData, CompanyData, CreditData, object_as_dict, db
from flask import current_app as app


@app.route('/personal_data', methods=['GET', 'POST'])
def personalData():
    if 'language' in request.args:
        personaldata = PersonalData(request.args.get('language'))
    else:
        personaldata = PersonalData('pl')
    if request.method == "POST":
        db.session.add(personaldata)
        db.session.commit()
    return jsonify(object_as_dict(personaldata))


@app.route('/company_data', methods=['GET', 'POST'])
def companyData():
    if 'language' in request.args:
        companydata = CompanyData(request.args.get('language'))
    else:
        companydata = CompanyData('pl')
    if request.method == "POST":
        db.session.add(companydata)
        db.session.commit()
    return jsonify(object_as_dict(companydata))


@app.route('/credit_data', methods=['GET', 'POST'])
def creditData():
    if 'language' in request.args:
        creditdata = CreditData(request.args.get('language'))
    else:
        creditdata = CreditData('pl')
    if request.method == "POST":
        db.session.add(creditdata)
        db.session.commit()
    return jsonify(object_as_dict(creditdata))


@app.route('/all_data', methods=['GET', 'POST'])
def allData():
    if 'language' in request.args:
        personaldata = PersonalData(request.args.get('language'))
        companydata = CompanyData(request.args.get('language'))
        creditdata = CreditData(request.args.get('language'))
    else:
        personaldata = PersonalData('pl')
        companydata = CompanyData('pl')
        creditdata = CreditData('pl')

    personaldatadictionary = object_as_dict(personaldata)
    companydatadictionary = object_as_dict(companydata)
    creditdatadictionary = object_as_dict(creditdata)
    output = []
    output.append(personaldatadictionary)
    output.append(companydatadictionary)
    output.append(creditdatadictionary)

    return jsonify(output)


@app.route('/delete_db', methods=['POST'])
def delete_database():
    db.drop_all()
    return jsonify('Success')


@app.route('/delete_personal_data', methods=['POST'])
def delete_personal_data():
    if 'id' in request.args:
        id = request.args.get("id")
        personaldata = PersonalData.query.filter_by(_id=id).first()
        if personaldata:
            db.session.delete(personaldata)
            db.session.commit()
        return jsonify("Success")
    else:
        return jsonify("Failed")


@app.route('/delete_credit_data', methods=['POST'])
def delete_credit_data():
    if 'id' in request.args:
        id = request.args.get("id")
        creditdata = CreditData.query.filter_by(_id=id).first()
        if creditdata:
            db.session.delete(creditdata)
            db.session.commit()
        return jsonify("Success")
    else:
        return jsonify("Failed")


@app.route('/delete_company_data', methods=['POST'])
def delete_company_data():
    if 'id' in request.args:
        id = request.args.get("id")
        companydata = CompanyData.query.filter_by(_id=id).first()
        if companydata:
            db.session.delete(companydata)
            db.session.commit()
        return jsonify("Success")
    else:
        return jsonify("Failed")


@app.route('/get_personal_data', methods=['GET'])
def get_personal_data():
    if 'id' in request.args:
        id = request.args.get("id")
        personaldata = PersonalData.query.filter_by(_id=id).first()
        if personaldata:
            return jsonify(object_as_dict(personaldata))
    else:
        return jsonify("Failed")


@app.route('/get_credit_data', methods=['GET'])
def get_credit_data():
    if 'id' in request.args:
        id = request.args.get("id")
        creditdata = CreditData.query.filter_by(_id=id).first()
        if creditdata:
            return jsonify(object_as_dict(creditdata))
    else:
        return jsonify("Failed")


@app.route('/get_company_data', methods=['GET'])
def get_company_data():
    if 'id' in request.args:
        id = request.args.get("id")
        companydata = CompanyData.query.filter_by(_id=id).first()
        if companydata:
            return jsonify(object_as_dict(companydata))
    else:
        return jsonify("Failed")


@app.route('/get_all_data', methods=['GET'])
def getAll():
    return jsonify("WIP")
