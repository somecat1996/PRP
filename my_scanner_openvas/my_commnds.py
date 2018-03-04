import commands


def make_request(user, password, xmlr):
    request = 'omp -u ' + user + ' -w ' + password + ' --xml=\''+xmlr+'\''
    return request


def get_configs(user, password):
    xmlr = '<get_configs/>'
    request = make_request(user, password, xmlr)
    output = commands.getoutput(request)
    return output


def create_target(user, password, name, hosts, comment):
    xmlr = '<create_target><name>'+name+'</name><hosts>'+hosts+'</hosts><comment>'+comment+'</comment></create_target>'
    request = make_request(user, password, xmlr)
    output = commands.getoutput(request)
    return output


def get_targets(user, password):
    xmlr = '<get_targets/>'
    request = make_request(user, password, xmlr)
    output = commands.getoutput(request)
    return output


def delete_target(user, password, id):
    xmlr = '<delete_target target_id="'+id+'"/>'
    request = make_request(user, password, xmlr)
    output = commands.getoutput(request)
    return output


def create_task(user, password, name, config_id, target_id, comment):
    xmlr = '<create_task><name>' + name + '</name><config id="' + config_id + '"/><target id="' + target_id + '"/><comment>'+comment+'</comment></create_task>'
    request = make_request(user, password, xmlr)
    output = commands.getoutput(request)
    return output


def get_task(user, password, id):
    xmlr = '<get_tasks task_id="'+id+'"/>'
    request = make_request(user, password, xmlr)
    output = commands.getoutput(request)
    return output


def get_tasks(user, password):
    xmlr = '<get_tasks/>'
    request = make_request(user, password, xmlr)
    output = commands.getoutput(request)
    return output


def delete_task(user, password, id):
    xmlr = '<delete_task task_id="'+id+'"/>'
    request = make_request(user, password, xmlr)
    output = commands.getoutput(request)
    return output


def start_task(user, password, id):
    xmlr = '<start_task task_id="'+id+'"/>'
    request = make_request(user, password, xmlr)
    output = commands.getoutput(request)
    return output


def pause_task(user, password, id):
    xmlr = '<pause_task task_id="'+id+'"/>'
    request = make_request(user, password, xmlr)
    output = commands.getoutput(request)
    return output

def resume_task(user, password, id):
    xmlr = '<resume_task task_id="'+id+'"/>'
    request = make_request(user, password, xmlr)
    output = commands.getoutput(request)
    return output

def stop_task(user, password, id):
    xmlr = '<stop_task task_id="'+id+'"/>'
    request = make_request(user, password, xmlr)
    output = commands.getoutput(request)
    return output


def get_results(user, password, id):
    xmlr = '<get_reports report_id="'+id+'"/>'
    request = make_request(user, password, xmlr)
    output = commands.getoutput(request)
    return output
