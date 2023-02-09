from use_cases.interfaces.object_interface import IObjectRepo


class ObjectRepo(IObjectRepo):
    def get_stats(self, api, oid, format):
        stats = api.query_objects(oid=oid, format=format)
        magstats = api.query_magstats(oid=oid)
        stats = stats.iloc[0]
        stats["mean_magpsf_r"] = magstats[1]["magmean"]
        stats["mean_magpsf_g"] = magstats[0]["magmean"]
        return stats
