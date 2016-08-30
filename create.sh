# These would be run on AWS

# Create index for team
curl -XPUT http://localhost:9200/team?pretty=true -d '
{
    "settings" : {
        "index" : {
            "number_of_shards" : 5,
            "number_of_replicas" : 0
        }
    }
}
'

# Create mapping
curl -XPUT http://localhost:9200/team/_mapping/profile?pretty=true -d '
{
    "profile" : {
        "properties" : {
            "role" : { "type" : "string", "store" : true },
            "name" : { "type" : "string", "store" : true },
            "desc" : { "type" : "string", "store" : true }
        }
    }
}
'