# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from alibabacloud_eventbridge.client import Client as EventBridgeClient
from alibabacloud_eventbridge import models as event_bridge_models
from alibabacloud_tea_console.client import Client as ConsoleClient
from alibabacloud_tea_util.client import Client as UtilClient


class Client(object):
    def __init__(self):
        pass

    @staticmethod
    def create_client():
        """
        Create client  初始化公共请求参数
        """
        config = event_bridge_models.Config(

        )
        # 您的AccessKey ID
        config.access_key_id = "<accessKeyId>"
        # 您的AccessKey Secret
        config.access_key_secret = "<accessKeySecret>"
        # 您的可用区ID
        config.endpoint = "<endpoint>"
        return EventBridgeClient(config)

    @staticmethod
    def create_event_bus_sample(client):
        try:
            create_event_bus_request = event_bridge_models.CreateEventBusRequest(

            )
            create_event_bus_request.event_bus_name = "demo-bus"
            response = client.create_event_bus(create_event_bus_request)
            ConsoleClient.log("--------------------Create bus success --------------------")
            ConsoleClient.log(UtilClient.to_jsonstring(response.to_map()))
        except Exception as error:
            ConsoleClient.log(error.message)

    @staticmethod
    def delete_event_bus_sample(client):
        try:
            # delete
            delete_event_bus_request = event_bridge_models.DeleteEventBusRequest(

            )
            delete_event_bus_request.event_bus_name = "demo-bus"
            client.delete_event_bus(delete_event_bus_request)
            ConsoleClient.log("--------------------Delete bus success --------------------")
        except Exception as error:
            ConsoleClient.log(error.message)

    @staticmethod
    def get_event_bus_sample(client):
        try:
            describe_event_bus_request = event_bridge_models.GetEventBusRequest(

            )
            describe_event_bus_request.event_bus_name = "demo-bus"
            de_scribe_response = client.get_event_bus(describe_event_bus_request)
            ConsoleClient.log("--------------------describe bus success --------------------")
            ConsoleClient.log(UtilClient.to_jsonstring(de_scribe_response.to_map()))
        except Exception as error:
            ConsoleClient.log(error.message)

    @staticmethod
    def list_event_bus_sample(client):
        try:
            list_event_buses_request = event_bridge_models.ListEventBusesRequest(

            )
            list_event_buses_request.limit = 100
            response = client.list_event_buses(list_event_buses_request)
            ConsoleClient.log("--------------------list bus success --------------------")
            ConsoleClient.log(UtilClient.to_jsonstring(response.to_map()))
        except Exception as error:
            ConsoleClient.log(error.message)

    @staticmethod
    def create_event_rule_sample(client):
        try:
            create_event_rule_request = event_bridge_models.CreateRuleRequest(

            )
            target_entry = event_bridge_models.TargetEntry(

            )
            target_entry.id = "1234"
            target_entry.endpoint = "http://www.baidu.com"
            target_entry_list = [
                target_entry
            ]
            # targetEntryList[0] =targetEntry;
            create_event_rule_request.rule_name = "myRule3"
            create_event_rule_request.event_bus_name = "demo-bus"
            create_event_rule_request.filter_pattern = "{\"source\":[\"acs.oss\"],\"type\":[\"oss:ObjectCreated:UploadPart\"]}"
            create_event_rule_request.status = "enable"
            create_event_rule_request.targets = target_entry_list
            response = client.create_rule(create_event_rule_request)
            ConsoleClient.log("--------------------create rule success--------------------")
            ConsoleClient.log(UtilClient.to_jsonstring(response.to_map()))
        except Exception as error:
            ConsoleClient.log(error.message)

    @staticmethod
    def delete_event_rule_sample(client):
        try:
            delete_rule_request = event_bridge_models.DeleteRuleRequest(

            )
            delete_rule_request.rule_name = "myRule3"
            delete_rule_request.event_bus_name = "demo-bus"
            client.delete_rule(delete_rule_request)
            ConsoleClient.log("--------------------delete rule success--------------------")
        except Exception as error:
            ConsoleClient.log(error.message)

    @staticmethod
    def enable_event_rule_sample(client):
        try:
            enable_event_rule_request = event_bridge_models.EnableRuleRequest(

            )
            enable_event_rule_request.rule_name = "myRule3"
            enable_event_rule_request.event_bus_name = "demo-bus"
            client.enable_rule(enable_event_rule_request)
            ConsoleClient.log("--------------------enable rule success--------------------")
        except Exception as error:
            ConsoleClient.log(error.message)

    @staticmethod
    def disable_event_rule_sample(client):
        try:
            disable_event_rule_request = event_bridge_models.DisableRuleRequest(

            )
            disable_event_rule_request.rule_name = "myRule3"
            disable_event_rule_request.event_bus_name = "demo-bus"
            client.disable_rule(disable_event_rule_request)
            ConsoleClient.log("--------------------disable rule success--------------------")
        except Exception as error:
            ConsoleClient.log(error.message)

    @staticmethod
    def describe_event_rule_sample(client):
        try:
            describe_event_rule_request = event_bridge_models.GetRuleRequest(

            )
            describe_event_rule_request.rule_name = "myRule3"
            describe_event_rule_request.event_bus_name = "demo-bus"
            client.get_rule(describe_event_rule_request)
            ConsoleClient.log("--------------------describe rule success--------------------")
        except Exception as error:
            ConsoleClient.log(error.message)

    @staticmethod
    def list_event_rule_sample(client):
        try:
            list_event_rules_request = event_bridge_models.ListRulesRequest(

            )
            list_event_rules_request.event_bus_name = "demo-bus"
            response = client.list_rules(list_event_rules_request)
            ConsoleClient.log("--------------------listRules rule success--------------------")
        except Exception as error:
            ConsoleClient.log(error.message)

    @staticmethod
    def update_event_rule_sample(client):
        try:
            update_event_rule_request = event_bridge_models.UpdateRuleRequest(

            )
            update_event_rule_request.event_bus_name = "demo-bus"
            update_event_rule_request.rule_name = "myRule3"
            update_event_rule_request.filter_pattern = "{\"source\":[\"acs.oss\"],\"type\":[\"oss:BucketQueried:GetBucketStat\"]}"
            client.update_rule(update_event_rule_request)
            ConsoleClient.log("--------------------update rule success--------------------")
        except Exception as error:
            ConsoleClient.log(error.message)

    @staticmethod
    def test_event_pattern__false(client):
        try:
            request = event_bridge_models.TestEventPatternRequest(

            )
            pattern = "{\n    \"source\": [\"acs.oss\"],\n    \"data\": {\n      \"b\": [1]\n    }\n}"
            json_data = "{\n        \"id\":\"51efe8e2-841f-4900-8ff5-3c6dfae1060e\",\n        \"source\":\"acs.oss\",\n        \"type\":\"oss:ObjectCreated:PostObject\",\n        \"dataschema\":\"http://taobao.com/test.json\",\n        \"subject\":\"acs:oss:cn-hangzhou:1234567:xls-papk/game_apk/123.jpg\",\n        \"aliyuneventbusname\":\"demo-bus\",\n        \"data\":{\n            \"a\":\"test\",\n            \"b\":1\n        }\n}"
            request.event = json_data
            request.event_pattern = pattern
            test_event_pattern_response = client.test_event_pattern(request)
            ConsoleClient.log("--------------------test event pattern --------------------")
            ConsoleClient.log(UtilClient.to_jsonstring(test_event_pattern_response.to_map()))
        except Exception as error:
            ConsoleClient.log(error.message)

    @staticmethod
    def test_event_pattern__true(client):
        try:
            request = event_bridge_models.TestEventPatternRequest(

            )
            pattern = "{\n    \"source\": [\"acs.oss\"],\n    \"data\": {\n      \"b\": [2]\n    }\n}"
            json_data = "{\n        \"id\":\"51efe8e2-841f-4900-8ff5-3c6dfae1060e\",\n        \"source\":\"acs.oss\",\n        \"type\":\"oss:ObjectCreated:PostObject\",\n        \"dataschema\":\"http://taobao.com/test.json\",\n        \"subject\":\"acs:oss:cn-hangzhou:1234567:xls-papk/game_apk/123.jpg\",\n        \"aliyuneventbusname\":\"demo-bus\",\n        \"data\":{\n            \"a\":\"test\",\n            \"b\":1\n        }\n}"
            request.event = json_data
            request.event_pattern = pattern
            test_event_pattern_response = client.test_event_pattern(request)
            ConsoleClient.log("--------------------test event pattern --------------------")
            ConsoleClient.log(UtilClient.to_jsonstring(test_event_pattern_response.to_map()))
        except Exception as error:
            ConsoleClient.log(error.message)

    @staticmethod
    def add_targets_sample(client):
        try:
            add_targets_request = event_bridge_models.CreateTargetsRequest(

            )
            add_targets_request.event_bus_name = "demo-bus"
            add_targets_request.rule_name = "myRule3"
            target_entry = event_bridge_models.TargetEntry(

            )
            target_entry.id = "1234"
            target_entry.endpoint = "http://www.baidu.com"
            list = [
                target_entry
            ]
            add_targets_request.targets = list
            response = client.create_targets(add_targets_request)
            ConsoleClient.log("--------------------Add targets success--------------------")
            ConsoleClient.log(UtilClient.to_jsonstring(response.to_map()))
        except Exception as error:
            ConsoleClient.log(error.message)

    @staticmethod
    def remove_targets_sample(client):
        try:
            remove_targets_response = event_bridge_models.DeleteTargetsRequest(

            )
            remove_targets_response.event_bus_name = "demo-bus"
            remove_targets_response.rule_name = "myRule3"
            list = [
                "1234"
            ]
            remove_targets_response.target_ids = list
            response = client.delete_targets(remove_targets_response)
            ConsoleClient.log("--------------------remove targets success--------------------")
            ConsoleClient.log(UtilClient.to_jsonstring(response.to_map()))
        except Exception as error:
            ConsoleClient.log(error.message)

    @staticmethod
    def list_targets_sample(client):
        try:
            list_targets_request = event_bridge_models.ListTargetsRequest(

            )
            list_targets_request.event_bus_name = "demo-bus"
            list_targets_request.rule_name = "myRule3"
            response = client.list_targets(list_targets_request)
            ConsoleClient.log("--------------------list targets success--------------------")
            ConsoleClient.log(UtilClient.to_jsonstring(response.to_map()))
        except Exception as error:
            ConsoleClient.log(error.message)

    @staticmethod
    def put_events(client):
        """
        PutEvents
        """
        event = event_bridge_models.CloudEvent(

        )
        event.datacontenttype = "application/json"
        event.data = UtilClient.to_bytes("test")
        event.id = "a5074581-7e74-4e4c-868f-47e7afdf8445"
        event.source = "acs.oss"
        event.specversion = "1.0"
        event.type = "oss:ObjectCreated:PostObject"
        event.time = "2020-08-24T13:54:05.965Asia/Shanghai"
        event.subject = "1.0"
        event.type = "acs:oss:cn-hangzhou:1234567:xls-papk/game_apk/123.jpg"
        event.extensions = {
            "aliyuneventbusname": "demo-bus"
        }
        try:
            resp = client.put_events([
                event
            ])
            ConsoleClient.log("--------------------Publish event to the aliyun EventBus--------------------")
            ConsoleClient.log(UtilClient.to_jsonstring(resp.to_map()))
        except Exception as error:
            ConsoleClient.log(error.message)

    @staticmethod
    def main(args):
        client = Client.create_client()
        Client.create_event_bus_sample(client)
        Client.put_events(client)
        Client.get_event_bus_sample(client)
        Client.list_event_bus_sample(client)
        Client.create_event_rule_sample(client)
        Client.enable_event_rule_sample(client)
        Client.disable_event_rule_sample(client)
        Client.describe_event_rule_sample(client)
        Client.list_event_rule_sample(client)
        Client.update_event_rule_sample(client)
        Client.test_event_pattern__false(client)
        Client.test_event_pattern__true(client)
        Client.add_targets_sample(client)
        Client.list_targets_sample(client)
        Client.remove_targets_sample(client)
        Client.delete_event_rule_sample(client)
        Client.delete_event_bus_sample(client)
