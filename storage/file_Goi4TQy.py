data = {'name':student.student.user.first_name+' '+student.student.user.last_name,
'father_name':student.student.fatherName,
'mother_name':student.student.motherName,
'roll_number':student.student.rollNumber,
'enrollment':student.student.enrollmentNumber,
'scholarship':student.student.scholarshipNumber,
'adhar':student.student.adhaarNumber,
'family_id':student.student.familyId,
'sssm_id':student.student.sssmId,
'gender':student.student.gender,
'medium':student.student.medium,
'dob':student.student.dateOfBirth,
'address':student.student.address,
'postal':student.student.postalCode,
'city':student.student.city.cityName,
'state':student.student.state.stateName,
'country':student.student.country.countryName,
'exam_name':exam.courseExam.exam.examName}


print(data)