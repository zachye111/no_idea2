@app_notes.route('/notes')
@login_required
def notes():


    return render_template('notes.html', user=user, notes=list_notes)